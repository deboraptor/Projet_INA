
"""
CRÉDITS :
@inproceedings{martin2020camembert,
  title={CamemBERT: a Tasty French Language Model},
  author={Martin, Louis and Muller, Benjamin and Ortiz Su{\'a}rez, Pedro Javier and Dupont, Yoann and Romary, Laurent and de la Clergerie, {\'E}ric Villemonte and Seddah, Djam{\'e} and Sagot, Beno{\^\i}t},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year={2020}
"""
	
import torch
import seaborn
import pandas as pd
from sklearn import metrics
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from transformers import CamembertForSequenceClassification, CamembertTokenizer, AdamW


#####################################################
# Encodage du texte
#####################################################

# Chargement du jeu de donnees
dataset = pd.read_csv("reviews_allocine_classification.csv")
 
reviews = dataset['review'].values.tolist()
sentiments = dataset['sentiment'].values.tolist()
 
# On charge l'objet "tokenizer"de camemBERT qui va servir a encoder
# 'camebert-base' est la version de camembert qu'on choisit d'utiliser
# 'do_lower_case' à True pour qu'on passe tout en miniscule
TOKENIZER = CamembertTokenizer.from_pretrained(
    'camembert-base',
    do_lower_case=True)
 
# La fonction batch_encode_plus encode un batch de donnees
encoded_batch = TOKENIZER.batch_encode_plus(reviews,
                                            add_special_tokens=True,
                                            max_length=MAX_LENGTH,
                                            padding=True,
                                            truncation=True,
                                            return_attention_mask = True,
                                            return_tensors = 'pt')
 
# On transforme la liste des sentiments en tenseur
sentiments = torch.tensor(sentiments)
 
# On calcule l'indice qui va delimiter nos datasets d'entrainement et de validation
# On utilise 80% du jeu de donnée pour l'entrainement et les 20% restant pour la validation
split_border = int(len(sentiments)*0.8)
 
 
train_dataset = TensorDataset(
    encoded_batch['input_ids'][:split_border],
    encoded_batch['attention_mask'][:split_border],
    sentiments[:split_border])
validation_dataset = TensorDataset(
    encoded_batch['input_ids'][split_border:],
    encoded_batch['attention_mask'][split_border:],
    sentiments[split_border:])
 
 
batch_size = 32
 
# On cree les DataLoaders d'entrainement et de validation
# Le dataloader est juste un objet iterable
# On le configure pour iterer le jeu d'entrainement de façon aleatoire et creer les batchs.
train_dataloader = DataLoader(
            train_dataset,
            sampler = RandomSampler(train_dataset),
            batch_size = batch_size)
 
validation_dataloader = DataLoader(
            validation_dataset,
            sampler = SequentialSampler(validation_dataset),
            batch_size = batch_size)

#####################################################
# Chargement du modèle
#####################################################

#  On la version pre-entrainee de camemBERT 'base'
model = CamembertForSequenceClassification.from_pretrained(
    'camembert-base',
    num_labels = 2)

#####################################################
# Hyperparamètres
#####################################################

optimizer = AdamW(model.parameters(),
                  lr = 2e-5, # Learning Rate
                  eps = 1e-8 # Epsilon)
epochs = 3

#####################################################
# Entraînement
#####################################################

# On va stocker nos tensors sur mon cpu : je n'ai pas mieux
device = torch.device("cpu")
 
# Pour enregistrer les stats a chaque epoque
training_stats = []
 
# Boucle d'entrainement
for epoch in range(0, epochs):
     
    print("")
    print(f'########## Epoch {epoch+1} / {epochs} ##########')
    print('Training...')
 
 
    # On initialise la loss pour cette epoque
    total_train_loss = 0
 
    # On met le modele en mode 'training'
    # Dans ce mode certaines couches du modele agissent differement
    model.train()
 
    # Pour chaque batch
    for step, batch in enumerate(train_dataloader):
 
        # On fait un print chaque 40 batchs
        if step % 40 == 0 and not step == 0:
            print(f'  Batch {step}  of 
{len(train_dataloader)}.')
         
        # On recupere les donnees du batch
        input_id = batch[0].to(device)
        attention_mask = batch[1].to(device)
        sentiment = batch[2].to(device)
 
        # On met le gradient a 0
        model.zero_grad()        
 
        # On passe la donnee au model et on recupere la loss et le logits (sortie avant fonction d'activation)
        loss, logits = model(input_id, 
                             token_type_ids=None, 
                             attention_mask=attention_mask, 
                             labels=sentiment)
 
        # On incremente la loss totale
        # .item() donne la valeur numerique de la loss
        total_train_loss += loss.item()
 
        # Backpropagtion
        loss.backward()
 
        # On actualise les parametrer grace a l'optimizer
        optimizer.step()
 
    # On calcule la  loss moyenne sur toute l'epoque
    avg_train_loss = total_train_loss / len(train_dataloader)   
 
    print("")
    print("  Average training loss: {0:.2f}".format(avg_train_loss))  
     
    # Enregistrement des stats de l'epoque
    training_stats.append(
        {
            'epoch': epoch + 1,
            'Training Loss': avg_train_loss,
        }
    )
 
print("Model saved!")
torch.save(model.state_dict(), "./sentiments.pt")

#####################################################
# Evaluation
#####################################################

def preprocess(raw_reviews, sentiments=None):
    encoded_batch = TOKENIZER.batch_encode_plus(raw_reviews,
                                                truncation=True,
                                                pad_to_max_length=True,
                                                return_attention_mask=True,
                                                return_tensors = 'pt')
    if sentiments:
        sentiments = torch.tensor(sentiments)
        return encoded_batch['input_ids'], encoded_batch['attention_mask'], sentiments
    return encoded_batch['input_ids'], encoded_batch['attention_mask']
 
def predict(reviews, model=model):
    with torch.no_grad():
        model.eval()
        input_ids, attention_mask = preprocess(reviews)
        retour = model(input_ids, attention_mask=attention_mask)
         
        return torch.argmax(retour[0], dim=1)
 
 
def evaluate(reviews, sentiments):
    predictions = predict(reviews)
    print(metrics.f1_score(sentiments, predictions, average='weighted', zero_division=0))
    seaborn.heatmap(metrics.confusion_matrix(sentiments, predictions))
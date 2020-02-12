# SCUT-Arabic-GEC
Neural Machine Translation (NMT) has been an out-performing and well-established model in the task of Grammar Error Correction (GEC). Arabic GEC is still growing because of some challenges, including scarcity of training sets and the complexity of Arabic language. Motivated by these challenges, we introduce an unsupervised NMT model for AGEC called SCUT AGEC. SCUT AGEC is a convolutional sequence-to-sequence model consisting of nine encoder-decoder layers with an attention mechanism. Furthermore, we developed a novel unsupervised method to generate a large-scale synthetic dataset based on confusion function to increase the amount of training set. Besides, proposed fine-tuning method to continue training the model with an authentic dataset to improve the performance and get more efficient results. Convolutional Natural Networks (CNN), gives our model the ability to joint feature extraction and classification in one task, and efficient capturing of the local context. Moreover, it is easy to obtain long-term dependencies because of convolutional layers staking. 


# Data set 
The datasets we used are Qatar Arabic Language Bank (QALB) from the second QALB shared task and Alwatan Arabic articles to generate the synthetic parallel corpus. The data of QALB corpus comes from the online commenters written at Aljazeera Arabic news channel articles. The release of QALB at ANLPACL 2015, includes non-native data comes from Arabic Learners Written Corpus (CERCLL) and some machine translation data is obtained from Wikipedia articles translated in Arabic language using Google translation. The training dataset contains 2 million words annotated and corrected by native Arabic speakers. 
Alwatan Arabic news articles corpus contains 20,291 articles and 10,000,000 words are categorized into six groups collected from the Omani newspaper. In our work, we generated a training dataset containing 18,061,610 million words in training and validation sets. The fine-tuning set consists of training and validation sets, and we used AQLB test set for testing. The whole training dataset contains 20,285,278 words and divided into a synthetic and authentic set. 

SCUT coupes Version 3 avaliable in : http://nlp.qatar.cmu.edu/qalb/ 
QALB 2015	avaliable in : 

# Model setting 
Our experiments are based on PyTorch-Fairseq  for training the convolutional sequence to sequence models with an attention mechanism. In the experiment, we used a 256-batch size for both sources and target embeddings. Furthermore, we applied BPE algorithm for vocabulary with 1000 tokens and dimension size is 300. Pre-trained embedding is applied using FastText with a Wikipedia corpus and a skip-gram model with a window size of 5 and 2 to 3 N-gram. Encoder and decoder have the same architecture, each one consisting of nine layers and the output of each layer is 512 dimensions.  Dropout is applied with the probability of 0.25 on the embeddings, each convolutional layer, and the output decoder. We applied Adam optimizer and trained each model for 50 epochs. The models were trained simultaneously on Python 3.6, NVidia GeForce GTX 1080 GPU, and CUDA 10 Production.






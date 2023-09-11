# enc-gen (Enhance n Generate 🤖)
An Intel SA Fall Hackathon Project!

![image](https://github.com/Utsav-Mehta/enc_gen/assets/81905399/2953c06f-4597-4584-a1d1-ba80c494c838)

- Description: A main problem of machine learning is being tried to solve through this project which is a huge dataset, or too little data for a specific class. These problems were found in the network intrusion detection dataset, and are being solved by merging of it with an AI-structured data generation reference kit, with active learning bridging between the two of them. In a nutshell, it has two functionality. 

1. Take a dataset (say network intrusion dataset), and use active learning to find N important rows, The user can choose N then generate samples similar to N using an AI structured reference kit, train the model again, and record results for all features set till N and show results at the end.
2. Take a dataset (small subset dataset in csv, say the csv containing rows of bening class) then use the AI structured reference kit to generate (PS the user just needs to pass the dataset path rest all work finding type, distribution, etc is done internally, which earlier used to be explicitly passed) The generated dataset can be directly downloaded as csv.

How to run?
```
docker build -t DockerFile.

docker run -p 8501:8501 DockerFile
```

Requirements specified in requirements.txt


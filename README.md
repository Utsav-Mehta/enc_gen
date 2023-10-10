# enc-gen (Enhance n Generate 🤖)
An Intel SA Fall Hackathon Project!

![image](https://github.com/Utsav-Mehta/enc_gen/assets/81905399/36c58b67-7db2-431e-b59a-068e047b9093)


Introducing Enc-Gen: Enhance n Generate System

Enc-Gen is a powerful solution designed to tackle the challenges faced in machine learning with simplicity and efficiency. This innovative system combines two essential functions: enhancing datasets for better analysis and generating new data for improved model performance. Let's break down what Enc-Gen does in a user-friendly way:

**1. Enhancing Datasets with Active Learning**:

Tailored Data Selection: Enc-Gen employs active learning techniques to identify a specific number of crucial data points, known as 'N', from large datasets. Users can customize 'N' according to their computing capabilities, making the process adaptable and efficient.

Smart Data Augmentation: Once these key data points are identified, Enc-Gen intelligently generates similar synthetic samples using advanced AI algorithms. This augmented dataset is carefully curated to enhance the quality and diversity of the original data.

**2. Generating New Data with Ease**:

Simplified Input: For smaller datasets or classes with limited samples, Enc-Gen simplifies the user experience. Just provide the basic dataset in CSV format, and Enc-Gen takes care of the rest.

Automated Data Generation: Enc-Gen's AI-driven algorithms work behind the scenes, analyzing the dataset and creating new, meaningful data. Users no longer need to worry about specifying data types or distributions; Enc-Gen handles everything internally.

Instant Access: The generated dataset is conveniently presented to the user in a downloadable CSV format. This ready-to-use data can seamlessly integrate into machine learning workflows, saving time and effort.

Benefits of Enc-Gen:

Efficiency: Enc-Gen automates complex processes, making it effortless to handle large datasets and generate synthetic data.
Flexibility: Users have the freedom to customize the active learning process based on their computational resources.
User-Friendly: Enc-Gen offers an intuitive interface, requiring minimal user input and ensuring a smooth experience.
Enhanced Results: By enhancing datasets and generating new data, Enc-Gen empowers machine learning models, leading to more accurate and reliable outcomes.
Enc-Gen simplifies the complexities of machine learning, making it accessible to everyone. Enhance your datasets, generate new insights, and supercharge your machine-learning projects with Enc-Gen today!


How to run?
```
docker build -t DockerFile.

docker run -p 8501:8501 DockerFile
```

Requirements specified in requirements.txt

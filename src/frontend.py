import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import enhance
import generator
import preprocessing
import pandas as pd


# Set the title
st.title("Enc-Gen Streamlit App")

selected_tab = st.sidebar.radio("Select a function", ["Enhance", "Generate", "Analysis","Benchmarks"])

if selected_tab == "Enhance":
    st.header("Enhance Options")
    
    # Text Input for File Path with Default Hint
    default_path = "/home/ubuntu/ai-super-reference-kit/ai-smart-generate/data/2021.02.17.csv"
    file_path = st.text_input("Enter the file path:", value="", placeholder=default_path)
    
    # Select Technology
    selected_technology = st.selectbox("Select Technology", ["stock", "intel"])
    
    # Text Input for Number of Iterations with Placeholder
    num_iterations = st.text_input("Number of rows to be selected:", value="", placeholder="e.g., 100")
    
    # Default Model Selection (Random Forest)
    selected_model = "Random Forest"

    # Default Preprocessing (Yes)
    perform_preprocessing = True
    
    # Text Input for Train Sample Size with Placeholder
    train_sample_size = st.text_input("Train Sample Size:", value="100", placeholder="e.g., 100")
    
    # Button to perform magic
    if st.button("Do Magic"):
        # Add your magic logic here when the button is clicked
        st.write("Magic is happening...")
        if selected_model == "Random Forest":
            s_model = "rf"
        
        # Placeholder data for scores (replace with your actual data)
        scores,time=enhance.enhance_al(dataset_path=file_path,env=selected_technology,numb_iters=int(num_iterations),model=s_model,do_preprocess=perform_preprocessing,train_sample_size=int(train_sample_size))
        
        # Plot scores vs len scores
        plt.figure(figsize=(8, 6))
        plt.plot(range(len(scores)), scores)
        plt.xlabel("Length of Scores")
        plt.ylabel("Scores")
        plt.title("Scores vs Length of Scores")
        st.pyplot(plt)

        st.write("Total time taken for enhancement using ",selected_technology,"is: ", time)

elif selected_tab == "Generate":
    st.header("Generate Options")
    
    # Text Input for Dataset Link
    dataset_path = st.text_input("Enter the dataset path")
    
    # Text Input for Size of Dataset to be Generated
    dataset_size = st.text_input("Size of the dataset to be generated:", placeholder="e.g., 100")
    
    # Button to Generate the Dataset
    if st.button("Generate Dataset"):
        # Add your dataset generation logic here (replace this with your actual code)
        st.write("Generating the dataset...")
        # Placeholder: Generating a sample dataset with random data
        generate_data=preprocessing.augment(df_path=dataset_path,samples_to_generate=int(dataset_size))
        generated_df = pd.DataFrame(generate_data)
        
        # Display the generated dataset
        st.write("Generated Dataset:")
        st.write(generated_df)
        
        # Button to Download the Generated Dataset
        st.write("Download the generated dataset:")
        csv = generated_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="generated_dataset.csv",
            key="download-button"
        )
    
elif selected_tab == "Analysis":
    st.header("Enhance Options")
    
    # Text Input for File Path with Default Hint
    default_path = "/home/ubuntu/ai-super-reference-kit/ai-smart-generate/data/2021.02.17.csv"
    file_path = st.text_input("Enter the file path:", value="", placeholder=default_path)
        
    # Text Input for Number of Iterations with Placeholder
    num_iterations = st.text_input("Number of rows to be selected:", value="", placeholder="e.g., 100")
    
    # Default Model Selection (Random Forest)
    selected_model = "Random Forest"

    # Default Preprocessing (Yes)
    perform_preprocessing = True
    
    # Text Input for Train Sample Size with Placeholder
    train_sample_size = st.text_input("Train Sample Size:", value="100", placeholder="e.g., 100")
    
    # Button to perform magic
    if st.button("Do comparsion"):
        st.write("Magic is happening...")
        if selected_model == "Random Forest":
            s_model = "rf"
        
        _,time_stock=enhance.enhance_al(dataset_path=file_path,env='stock',numb_iters=int(num_iterations),model=s_model,do_preprocess=perform_preprocessing,train_sample_size=int(train_sample_size))
        _,time_intel=enhance.enhance_al(dataset_path=file_path,env='intel',numb_iters=int(num_iterations),model=s_model,do_preprocess=perform_preprocessing,train_sample_size=int(train_sample_size))

        plt.figure(figsize=(8, 6))
        colors = ['#0071C5', '#003366']  # Use Intel's logo color for the second bar
        plt.bar(['stock','intel'],[time_stock,time_intel],color=colors)
        plt.xlabel("Technology")
        plt.ylabel("Time")
        plt.title("Time vs Technology")
        st.pyplot(plt)

elif selected_tab == "Benchmarks":
    st.header("Benchmarks")
    st.write('Active Learning')
    st.image("assets\\download.png")
    st.write('Intel vs Stock')
    st.image("assets\\intel-vs-stock.png")
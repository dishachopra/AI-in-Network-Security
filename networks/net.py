import streamlit as st
# Set a black background for the entire app
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("AI in network Security")
st.header("Data Statistics")


image_path = "networks/normalVSattack.png"

# Display the image using st.image
st.image(image_path, caption='Your Image Caption', use_column_width=True)
image_path1 = "networks/top5attacks.png"
st.image(image_path1, caption='Your Image Caption', use_column_width=True)
image_path2 = "networks/noOfrestAttacks.png"
st.image(image_path2, caption='Your Image Caption', use_column_width=True)

st.subheader("Feature Importance")
#heading for feature importance
st.header("Binary Classification")
image_path4 = "networks/featureImpBin.png"
st.image(image_path4, caption='Your Image Caption', use_column_width=True)

image_paths = {
    'Random Forest': 'networks/rfBin.png',
    'Naive Bais': 'networks/naiveBin.png',
    'Logisic Regression': 'networks/lrBin.png',
    'MLP': 'networks/mlpBin.png',
    'K Nearest Neighbors': 'networks/knnBin.png',
    'Variational Autoencoders': 'networks/vaeBin.png',
    'Convolutional Neural Networks': 'networks/cnnBin.png',
    'Isolation Forest': 'networks/isolationBin.png',
    'Adaboost': 'networks/AdaBoostBin.png'
    # Add more images as needed
}

# Create a selectbox to choose from the available images
selected_image_name = st.selectbox("Select a model for Binary Classification", list(image_paths.keys()))

# Use an if-else statement to determine the selected image path
if selected_image_name in image_paths:
    selected_image_path = image_paths[selected_image_name]
    st.image(selected_image_path, caption=f'Selected Image: {selected_image_name}', use_column_width=True)
else:
    st.write("Image not found.")
st.subheader("Feature Importance")
#heading for feature importance
st.header("Multiclass Classification")
image_path5 = "networks/featureImpMulti.png"
st.image(image_path5, caption='Your Image Caption', use_column_width=True)

image_paths = {
    'Random Forest': 'networks/rfMulti.png',
    'Naive Bais': 'networks/naiveMulti.png',
    'Logisic Regression': 'networks/lrMulti.png',
    'MLP': 'networks/mlpMulti.png',
    'K Nearest Neighbors': 'networks/knnMulti.png'
    }
image_path6 = "networks/attacks.png"
st.image(image_path6, caption='Your Image Caption', use_column_width=True)

# Create a selectbox to choose from the available images
selected_image_name = st.selectbox("Select a model for Multi Classification", list(image_paths.keys()))

# Use an if-else statement to determine the selected image path
if selected_image_name in image_paths:
    selected_image_path = image_paths[selected_image_name]
    st.image(selected_image_path, caption=f'Selected Image: {selected_image_name}', use_column_width=True)
else:
    st.write("Image not found.")

# Dictionary mapping attack names to their feature importance images
image_paths1 = {
    'Neptune': 'networks/FIneptune.png',
    'Satan': 'networks/FISatan.png',
    'Smurf': 'networks/FIsmurf.png',
    'IPSweep': 'networks/IPSweep.png',
    'PortSweep': 'networks/portSweep.png'
}

# Create a selectbox to choose from the available attacks
selected_attack_name = st.selectbox("Select an attack to see its feature importance", list(image_paths1.keys()))

# Use an if-else statement to determine the selected image path
if selected_attack_name in image_paths1:
    selected_image_path = image_paths1[selected_attack_name]
    st.image(selected_image_path, caption=f'Selected Attack: {selected_attack_name}', use_column_width=True)
else:
    st.write("Image not found.")





    

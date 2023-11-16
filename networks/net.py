import streamlit as st
st.title("AI in network Security")
# Assuming you have a downloaded image file path
#Add heading in middle data statistics
st.header("Data Statistics")


image_path = "/Users/disha/Desktop/networks/normalVSattack.png"

# Display the image using st.image
st.image(image_path, caption='Your Image Caption', use_column_width=True)
image_path1 = "/Users/disha/Desktop/networks/top5attacks.png"
st.image(image_path1, caption='Your Image Caption', use_column_width=True)
image_path2 = "/Users/disha/Desktop/networks/noOfrestAttacks.png"
st.image(image_path2, caption='Your Image Caption', use_column_width=True)

st.subheader("Feature Importance")
#heading for feature importance
st.header("Binary Classification")
image_path4 = "/Users/disha/Desktop/networks/featureImpBin.png"
st.image(image_path4, caption='Your Image Caption', use_column_width=True)

image_paths = {
    'Random Forest': '/Users/disha/Desktop/networks/rfBin.png',
    'Naive Bais': '/Users/disha/Desktop/networks/naiveBin.png',
    'Logisic Regression': '/Users/disha/Desktop/networks/lrBin.png',
    'MLP': '/Users/disha/Desktop/networks/mlpBin.png',
    'K Nearest Neighbors': '/Users/disha/Desktop/networks/knnBin.png',
    'Variational Autoencoders': '/Users/disha/Desktop/networks/vaeBin.png',
    'Convolutional Neural Networks': '/Users/disha/Desktop/networks/cnnBin.png',
    'Isolation Forest': '/Users/disha/Desktop/networks/isolationBin.png',
    'Adaboost': '/Users/disha/Desktop/networks/AdaBoostBin.png'
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
image_path5 = "/Users/disha/Desktop/networks/featureImpMulti.png"
st.image(image_path5, caption='Your Image Caption', use_column_width=True)

image_paths = {
    'Random Forest': '/Users/disha/Desktop/networks/rfMulti.png',
    'Naive Bais': '/Users/disha/Desktop/networks/naiveMulti.png',
    'Logisic Regression': '/Users/disha/Desktop/networks/lrMulti.png',
    'MLP': '/Users/disha/Desktop/networks/mlpMulti.png',
    'K Nearest Neighbors': '/Users/disha/Desktop/networks/knnMulti.png'
    }
image_path6 = "/Users/disha/Desktop/networks/attacks.png"
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
    'Neptune': '/Users/disha/Desktop/networks/FIneptune.png',
    'Satan': '/Users/disha/Desktop/networks/FISatan.png',
    'Smurf': '/Users/disha/Desktop/networks/FIsmurf.png',
    'IPSweep': '/Users/disha/Desktop/networks/IPSweep.png',
    'PortSweep': '/Users/disha/Desktop/networks/[ortSweep].png'
}

# Create a selectbox to choose from the available attacks
selected_attack_name = st.selectbox("Select an attack to see its feature importance", list(image_paths1.keys()))

# Use an if-else statement to determine the selected image path
if selected_attack_name in image_paths1:
    selected_image_path = image_paths1[selected_attack_name]
    st.image(selected_image_path, caption=f'Selected Attack: {selected_attack_name}', use_column_width=True)
else:
    st.write("Image not found.")





    
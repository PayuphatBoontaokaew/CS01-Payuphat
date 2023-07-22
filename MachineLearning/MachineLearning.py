from mlforkids import MLforKidsImageProject
# treat this key like a password and keep it secret!
key = "b0cabba0-2838-11ee-815a-63593f9586039c4a78d5-e47f-472b-8067-6c18a16fcce5"

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("my-test-image.jpg")
label = demo["class_name"]
confidence = demo["confidence"]
# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))


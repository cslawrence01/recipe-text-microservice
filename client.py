

import zmq

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

byte_string = b'Vegetarian Stir-Fry Recipe:\n\nIngredients:\n- 1 bell pepper, sliced\n- 1 onion, sliced\n- 1 cup broccol' \
              b'i florets\n- 1 cup sliced mushrooms\n- 1 cup snap peas\n- 2 cloves garlic, minced\n- 2 tablespoons soy ' \
              b'sauce\n- 1 tablespoon sesame oil\n- 1 tablespoon cornstarch\n- 1/4 cup vegetable broth\n- Cooked rice or' \
              b' noodles for serving\n\nInstructions:\n1. In a small bowl, mix together soy sauce, sesame oil, cornstarch' \
              b', and vegetable broth. Set aside.\n2. In a large skillet or wok, heat some oil over medium-high heat. ' \
              b'Add the garlic and cook for about 1 minute.\n3. Add the bell pepper, onion, broccoli, mushrooms, and ' \
              b'snap peas to the skillet. Stir-fry for about 5-7 minutes until the vegetables are tender-crisp.\n4. ' \
              b'Pour the soy sauce mixture over the vegetables and stir to combine. Cook for another 2-3 minutes until ' \
              b'the sauce has thickened.\n5. Serve the stir-fry over cooked rice or noodles. Enjoy your delicious and healthy meal!'

socket.send(byte_string)

# client must receive a message back from the server to comply with the request-reply pattern
message = socket.recv()
print(message)

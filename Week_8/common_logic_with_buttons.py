import streamlit as st 

st.title("Common Logic With Buttons")

"""
## Show temporary message with button
# """
animal_shelter = ['cat', 'dog', 'rabbit', 'bird'] 

animal = st.text_input('Type an animal') 

if st.button('Check availability'): 
	have = animal.lower() in animal_shelter 
	f'We have that {animal}!' if have else f'We don\'t have that {animal}.'
 
"""
## Stateful button

If you want a clicked button to continue to be True, 
create a value in st.session_state and use the button to set that value to True in a callback.
"""

if 'clicked' not in st.session_state: 
	st.session_state.clicked = False 
	
def click_button(): 
	st.session_state.clicked = True 
	
st.button('Click me', on_click=click_button) 

if st.session_state.clicked: 
	# The message and nested widget will remain on the page 
	st.write('Button clicked!') 
	st.slider('Select a value')
 
"""
## Toggle button
In this example, we use st.button to toggle another widget on and off. 
By displaying st.slider conditionally on a value in st.session_state, the user can interact with the slider without it disappearin
"""
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')
    
"""
## Buttons to modify st.session_state

If you modify st.session_state inside of a button, 
you must consider **WHERE** that button is within the script.
"""

# import streamlit as st 
# import pandas as pd 

# if 'name' not in st.session_state: 
# 	st.session_state['name'] = 'John Doe' 
	
# st.header(st.session_state['name']) 

# if st.button('Jane'): 
# 	st.session_state['name'] = 'Jane Doe' 
	
# if st.button('John'): 
# 	st.session_state['name'] = 'John Doe' 
	
# st.header(st.session_state['name'])


"""
## Logic used in a callback

Callbacks are a clean way to modify st.session_state. 
Callbacks are executed as a prefix to the script rerunning, 
so the position of the button relative to accessing data is not important.
"""


# import streamlit as st 
# import pandas as pd 

# if 'name' not in st.session_state: 
# 	st.session_state['name'] = 'John Doe' 
	
# def change_name(name): 
# 	st.session_state['name'] = name 
	
# st.header(st.session_state['name']) 

# st.button('Jane', on_click=change_name, args=['Jane Doe']) 
# st.button('John', on_click=change_name, args=['John Doe']) 

# st.header(st.session_state['name'])

"""
## Buttons to modify or reset other widgets

When a button is used to modify or reset another widget, 
it is the same as the above examples to modify st.session_state. 

However, an extra consideration exists: you cannot modify a key-value pair in st.session_state 
if the widget with that key has already been rendered on the page for the current script run.
"""

"""
### Option 1: Use a key for the button and put the logic *before* the widget

If you assign a key to a button, you can condition code on a button's state by using its value in st.session_state.
This means that logic depending on your button can be in your script before that button.

In the following example, we use the .get() method on st.session_state 
because the keys for the buttons will not exist when the script runs for the first time. 
The .get() method will return False if it can't find the key. Otherwise, it will return the value of the key.

"""

# Use the get method since the keys won't be in session_state 
# on the first script run 
# if st.session_state.get('clear'): 
# 	st.session_state['name'] = '' 
	
# if st.session_state.get('streamlit'): 
# 	st.session_state['name'] = 'Streamlit' 
	
# st.text_input('Name', key='name') 

# st.button('Clear name', key='clear') 
# st.button('Streamlit!', key='streamlit')

"""
### Option2: Use call back

"""

# st.text_input('Name', key='name') 

# def set_name(name): 
# 	st.session_state.name = name 
	
# st.button('Clear name', on_click=set_name, args=['']) 
# st.button('Streamlit!', on_click=set_name, args=['Streamlit'])

"""
### Option3: Use Containers

# """
# import streamlit as st 

# begin = st.container() 

# if st.button('Clear name'): 
# 	st.session_state.name = '' 
	
# if st.button('Streamlit!'): 
# 	st.session_state.name = ('Streamlit') 
	
# # The widget is second in logic, but first in display 
# begin.text_input('Name', key='name')

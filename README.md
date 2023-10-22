# About Pet Budget Simulator
## Inspiration
Pet Budget Simulator was inspired by Capital One's challenge of Best Financial Hack combined with our love for our pets. David and Aidan are brothers who have an extremely cute cat named Yogurt!
## What it does
Our project aims to provide a intuitive and easy way to keep track of pet spending across different categories. Furthermore, users will be able to compare product prices and see how relatively expensive their product is compared to other products in the same category.
## How we built it
We built our product using Streamlit. Streamlit is a Python library that allowed us to rapidly develop a web application with a user-friendly interface. It made the process of creating interactive data apps and dashboards incredibly efficient. With Streamlit, we were able to focus on building the features and functionality of our product while the framework took care of the web development aspects. This not only saved us time but also ensured a smooth user experience.
Streamlit is not inherently stateful (user input would disapear upon page refresh). Therefore we used session_state API to add statefullness. Session_state allows us to directly create, access, change variables as opposed to RESTful API’s ‘GET’, ‘POST’, etc.
During the development process, we used Github codespaces connected with Streamlit. This allowed us to see live coding changes, vastly speeding up the prototyping/frontend development process.
To allow the user to compare product prices, Pet Budget Simulator uses a dataset downloaded from Kaggle called "Amazon pet supplies data". To visualize this data, we used Matplotlib to display budgeting results.
## Challenges we ran into
We initially wanted to develop and add an html component to separate front and back end development. However, after some experimenting we learned that Streamlit is primarily designed for data apps, and it does not handle external CSS and assets in the same way a traditional web server or framework does. We had to pivot into developing frontend features entirely in Streamlit.
The "Amazon pet supplies data" we downloaded only provided certain fields such as the product name, price, product ID, etc. but did not have a category column. We needed each product to be sorted into a category in order to compare their prices. Therefore (by the suggestion of a mentor Cole), we developed a procedure to curate the data to extract the product category from the product name. 
## Accomplishments that we're proud of

## What we learned

## What's next for Pet Budget Simulator

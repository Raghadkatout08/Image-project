# Image-project

## Overview

Image Project is a Django-based web application that allows users to explore and discover a collection of food images. The application uses Django for the backend and provides a RESTful API with Django REST framework. The application is containerized using Docker for ease of deployment.

## Features

- Browse a collection of food images.
- View details like views, downloads, likes, and comments for each image.

## Requirements

- Docker
- Docker Compose

## Installation

### Clone the repository
```git clone https://github.com/your-username/image-project.git```

```cd image-project```

### Environment Variables

Create a `.env` file in the root of the project with the following content:
```PIXABAY_API_KEY=your_pixabay_api_key```


### Dependencies

Create a `requirements.txt` file in the root of your project and add the following dependencies:
 
`asgiref==3.8.1`
``certifi==2024.7.4``
`charset-normalizer==3.3.2`
`Django==5.0.7`
`idna==3.7`
`python-decouple==3.8`
`requests==2.32.3`
`sqlparse==0.5.1`
`urllib3==2.2.2`


## Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss any changes you would like to make.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Pixabay API](https://pixabay.com/api/docs/)
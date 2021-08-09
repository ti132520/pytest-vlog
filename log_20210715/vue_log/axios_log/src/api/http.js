import axios from "axios";
var token = localStorage.getItem('token')

var instance = axios.create({
    headers: {
        'Content-Type': 'application/json',
        'csrfmiddlewaretoken': token,
        'X-CSRFToken': token
    },
    baseURL: 'http://127.0.0.1:8000',
})

export default instance
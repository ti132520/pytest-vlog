import axios from "axios";
var token = localStorage.getItem('token')

var instance = axios.create({
    headers: {
        'Content-Type': 'application/json',
        'csrfmiddlewaretoken': token,
        'X-CSRFToken': token
    },
    baseURL: 'http://vue-saas.ti132520.fun',
})

export default instance
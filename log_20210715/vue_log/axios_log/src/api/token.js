import axios from "./http";

const token = {
    get_token(){
        return axios({
            method:'get',
            url: 'get_token',
        })
    }
}

export default token

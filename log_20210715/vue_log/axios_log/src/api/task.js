import axios from "./http";


const task = {
    get_task() {
        return axios({
            method: 'get',
            url: '/task'
        })
    },
    add_task(data) {
        console.log(data);
        return axios({
            method: 'post',
            url: '/task',
            data: data
        })
    }
}


export default task
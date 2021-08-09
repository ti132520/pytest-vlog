import axios from "./http";

const testcase = {
    getTestcase(){
        return axios({
            method: 'get',
            url: 'testcase',
            data: {

            }
        })
    },
    deleteTestcase(data){
        return axios({
            method: 'delete',
            url: 'testcase',
            data: data
        })
    },
    updateTestcase(data){
        return axios({
            method: 'put',
            url: 'testcase',
            data:data
        })
    },
    addTestcase(data){
        return axios({
            method: 'post',
            url: 'testcase',
            data:data
        })
    },

}

export default testcase
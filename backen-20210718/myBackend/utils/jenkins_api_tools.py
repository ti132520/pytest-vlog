from jenkinsapi.jenkins import Jenkins


class Tools:
    __base_url = "http://118.121.198.166:8081"
    __username = "ti132520"
    __token = "118448ed4702b70ea89c029a0b2f06650f"
    __jenkins = Jenkins(__base_url, __username, __token)

    @classmethod
    def get_jobs(cls):
        return cls.__jenkins.keys()

    @classmethod
    def invoke(cls, task, job_name='test'):
        job = cls.__jenkins.get_job(job_name)
        job.invoke(build_params={"task": task})
        last_num = job.get_last_buildnumber()
        print(last_num)

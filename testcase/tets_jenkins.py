from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    jenkins = Jenkins(
        'http://129.211.167.92:8020/',
        username='manager',
        password='11e25651ef39f57100d35173b9e85edb49'
    )


    jenkins['testcase'].invoke(
        securitytoken='11e25651ef39f57100d35173b9e85edb49',
        build_params={
            'testcases': '.'
        })
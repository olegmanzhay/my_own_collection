# my_own_collection

## Шаг 1. В виртуальном окружении создайте новый my_own_module.py файл.  
/home/admin-oleg/Desktop/Netology/my_own_collection/ansible/library/my_own_module.py  

## Шаг 3-5. Заполните файл в соответствии с требованиями Ansible так, чтобы он выполнял основную задачу: module должен создавать текстовый файл на удалённом хосте по пути, определённом в параметре path, с содержимым, определённым в параметре content.    

Код до плейбуки: /home/admin-oleg/Desktop/Netology/my_own_collection/ansible/test_module.yml

```
def run_module():
    # Define module arguments
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # Initialize result dictionary
    result = dict(
        changed=True,
        result=''
    )

    # Create AnsibleModule instance
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Extract parameters
    file_path = module.params['path']
    file_content = module.params['content']

    # Handle check mode
    if module.check_mode:
        result['result'] = "File would be created/overwritten"
        module.exit_json(**result)

    # Create or overwrite the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        result['result'] = "File created/overwritten successfully"
    except Exception as e:
        module.fail_json(msg=f"Failed to write file: {str(e)}", **result)

    # Return results
    module.exit_json(**result)

```

## При таком варианте кода нет иденпотентности, так как при выполнении модуля происходит 
```
TASK [Create test file] ******************************************************************************************************************************************************************************
changed: [localhost] => {"changed": true, "result": "File created/overwritten successfully"}
```

## Шаг 6. Проверьте через playbook на идемпотентность.

После корректировки my_own_collection.py получил 
```
TASK [Create test file] ******************************************************************************************************************************************************************************
ok: [localhost] => {"changed": false, "result": "File already exists with correct content"}
```

## Шаг 15  
ссылки на collection: /home/admin-oleg/Desktop/Netology/my_own_collection/ansible/my_own_namespace/yandex_cloud_elk  
tar.gz : /home/admin-oleg/Desktop/Netology/my_own_collection/ansible/my_own_namespace/my_own_namespace-yandex_cloud_elk-1.0.0.tar.  


Результат работы модуля (иденпотентность проверена)  
```
PLAYBOOK: test_collection.yml ************************************************************************************************************************************************************************
1 plays in test_collection.yml

PLAY [Test installed collection] *********************************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************************************
task path: /home/admin-oleg/Desktop/Netology/my_own_collection/ansible/test_collection.yml:2
<127.0.0.1> ESTABLISH LOCAL CONNECTION FOR USER: admin-oleg
<127.0.0.1> EXEC /bin/sh -c 'echo ~admin-oleg && sleep 0'
<127.0.0.1> EXEC /bin/sh -c '( umask 77 && mkdir -p "` echo /home/admin-oleg/.ansible/tmp `"&& mkdir "` echo /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941865.518649-17680-39516705830972 `" && echo ansible-tmp-1771941865.518649-17680-39516705830972="` echo /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941865.518649-17680-39516705830972 `" ) && sleep 0'
Using module file /usr/lib/python3/dist-packages/ansible/modules/setup.py
<127.0.0.1> PUT /home/admin-oleg/.ansible/tmp/ansible-local-17648y92ehz0d/tmp8vr3a7j0 TO /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941865.518649-17680-39516705830972/AnsiballZ_setup.py
<127.0.0.1> EXEC /bin/sh -c 'chmod u+rwx /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941865.518649-17680-39516705830972/ /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941865.518649-17680-39516705830972/AnsiballZ_setup.py && sleep 0'
<127.0.0.1> EXEC /bin/sh -c '/usr/bin/python3 /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941865.518649-17680-39516705830972/AnsiballZ_setup.py && sleep 0'
<127.0.0.1> EXEC /bin/sh -c 'rm -f -r /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941865.518649-17680-39516705830972/ > /dev/null 2>&1 && sleep 0'
ok: [localhost]

TASK [Use custom module directly] ********************************************************************************************************************************************************************
task path: /home/admin-oleg/Desktop/Netology/my_own_collection/ansible/test_collection.yml:7
<127.0.0.1> ESTABLISH LOCAL CONNECTION FOR USER: admin-oleg
<127.0.0.1> EXEC /bin/sh -c 'echo ~admin-oleg && sleep 0'
<127.0.0.1> EXEC /bin/sh -c '( umask 77 && mkdir -p "` echo /home/admin-oleg/.ansible/tmp `"&& mkdir "` echo /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941866.3857372-17812-126766948235175 `" && echo ansible-tmp-1771941866.3857372-17812-126766948235175="` echo /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941866.3857372-17812-126766948235175 `" ) && sleep 0'
Using module file /home/admin-oleg/.ansible/collections/ansible_collections/my_own_namespace/yandex_cloud_elk/plugins/modules/my_own_module.py
<127.0.0.1> PUT /home/admin-oleg/.ansible/tmp/ansible-local-17648y92ehz0d/tmp3z70p1lg TO /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941866.3857372-17812-126766948235175/AnsiballZ_my_own_module.py
<127.0.0.1> EXEC /bin/sh -c 'chmod u+rwx /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941866.3857372-17812-126766948235175/ /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941866.3857372-17812-126766948235175/AnsiballZ_my_own_module.py && sleep 0'
<127.0.0.1> EXEC /bin/sh -c '/usr/bin/python3 /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941866.3857372-17812-126766948235175/AnsiballZ_my_own_module.py && sleep 0'
<127.0.0.1> EXEC /bin/sh -c 'rm -f -r /home/admin-oleg/.ansible/tmp/ansible-tmp-1771941866.3857372-17812-126766948235175/ > /dev/null 2>&1 && sleep 0'
ok: [localhost] => {
    "changed": false,
    "invocation": {
        "module_args": {
            "content": "This file was created using the installed collection",
            "path": "/tmp/test_from_installed_collection.txt"
        }
    },
    "result": "File already exists with correct content"
}

TASK [Show module result] ****************************************************************************************************************************************************************************
task path: /home/admin-oleg/Desktop/Netology/my_own_collection/ansible/test_collection.yml:13
ok: [localhost] => {
    "module_result": {
        "changed": false,
        "failed": false,
        "result": "File already exists with correct content"
    }
}

PLAY RECAP *******************************************************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
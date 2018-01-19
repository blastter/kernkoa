#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kernkoa import * #imports every varible from kernkoa (databases, loader, etc...).

# it's jus a normal class, wich has methods to be executed asynchronously
class asyncclass:
    
    # Trigger method to execute de big task.
    def triggerfunction(self, params = None):
        # exeTask is a method defined un KernKoa to execute async tasks
        #   It gets the name of the method to be executed un a string and the paramenters from
        #   the request (get or post).
        task = exeTask(self, "asyncfunction_celery", params)
        # The result of the method in this case is a URL to get the status of the Task.
        #   If the task has been succesfully procesed, the same link will give you the result
        return "<a href='" + config.url + "status/" + task["id"] + "'>Async Test"

    # Method to be executed asynchronously
    #   As you can see un the definition of the method you input celery_instance ans params
    #       - The params are the post parameters.
    #       - celery_instance is the connection to the task manager to update the status of the task.
    #           like when you change the done percentage of the task. 
    def asyncfunction_celery(self, celery_instance = None, params = None):
        #Counts to 10 with 2 seconds of delay so the task thread gets stuck, and the m
        for i in range(0,10):
            # if celery instance exists or if it's instansiated, it will update the result, if not, you are
            # runing on the main thread.
            if celery_instance:
                # Update of the status of the task.
                celery_instance.update_state(state="inProgress", meta={"number":i+1, "title": "Contando con 2 segundos de desfase hasta 10"})
            # Two second delay
            time.sleep(2)
            print(i)
        # The result of the async task.
        return i + 1
        
from opencrowd.model.server import Opencrowd

opencrowd = Opencrowd.regenerate()

print("Project Ids: {}".format(opencrowd.list_project_ids()))
print("Task Ids: {}".format(opencrowd.list_task_ids()))
print("HIT Ids: {}".format(opencrowd.list_HIT_ids()))
print("Assignment IDs: {}".format(opencrowd.list_assignment_ids()))
print("Question IDs: {}".format(opencrowd.list_question_ids()))
print("Section IDs: {}".format(opencrowd.list_section_ids()))
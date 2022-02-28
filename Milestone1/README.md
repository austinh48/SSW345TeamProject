Problem Statement: 
The problem that our group wishes to address is procrastination/poor organization. A lot of students struggle with keeping on top of their homework/assignments and we want to create a bot that helps solve this issue. The reason that procrastination is such a big problem is because it is so easy to push a homework assignment to the next day or forget about a long term project. With our bot the goal is to have the bot send automatic reminders for assignments that you have, with the reminders being more/less frequent depending on how close the assignment is. With "frequent" reminders about your future assignments it will be much harder to procrastinate/forget about assignments.

Description:
This bot will use a canvas api to take assignment names and due dates and send out reminders. As of now, we're thinking about using discord in order to send notifications but we might try and use something else. The bot will send notifications for the assignment, and they will get more frequent as the due date gets closer. For example, if there is an assignment due in 2 weeks, the bot will send a reminder a week out, another one 3 days prior, and another the day before it's due. We also might add customization to the notification system that way you can set if you want more/less frequent notifications. The bot is a good solution to this problem because the main problem with assignments that are due down the line is remembering that the assignment is due. With the reminders, users will remember that they have the assignment due. Our bot will have a feature that allows you to make the bot more/less friendly to make it seem like you're talking to a friend or just getting notifications.

Use Cases:
  Use Case: Canvas Api
  1. Preconditions
      Bot must have access to the canvas page.
  3. Main Flow
      Bot will take a task from canvas [S1] and create a prioritized to-do list [S2]. Users will also be able to input their own tasks [S3].
  3. Subflows
      [S1] Bot will strip info from canvas, user will approve it.
      [S2] Bot will organize the to-do list by the deadlines given to the assignments.
      [S3] Bot will take a name, and a due date for the task.
  4. Alternative Flows
      [E1] Users can skip connecting canvas and input all their tasks themselves.
  Use Case: Sending Messages
  1. Preconditions
      None
  2. Main Flow
      Bot will keep track of due dates [S1]. It will send reminders at preset time intervals untill the task is marked completed [S2]. The messages from the bot will have a range of friendliness, as set by the user [S3]
  3. Subflows
      [S1] Due dates will be taken from canvas and the user.
      [S2] Messeges will be sent to the user regularly until they mark off the assignment.
      [S3] The user will be able to determine the tone of the messeges.
  4. Alternative Flows
      [E1] If no bot friendliness is set, the bot will default to a neutral tone.

Design Sketches: 


Architecture Design:


Tagline: RemindBot


Team: 
austinh48 - sean hodges
cmclaug - Caitlin McLaughlin

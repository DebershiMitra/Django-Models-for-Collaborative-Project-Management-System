# Django-Models-for-Collaborative-Project-Management-System
This Django models script lays the foundation for a collaborative project management system.
Let's break down each component:

Team Model (commented out):
Represents a team within the system.

Attributes:
name: CharField for the team name.
desc: CharField for a brief description of the team.
user: ForeignKey relationship with the Django User model representing the team owner.
created_on: DateTimeField for the creation date of the team.
String representation: Returns the name of the team.

Project Model:
Represents a project within the system.

Attributes:
name: CharField for the project name.
desc: CharField for a brief description of the project.
start_date: DateTimeField for the start date of the project.
user: ManyToManyField relationship with the Django User model representing project members.
String representation: Returns the name of the project.

Conversation Model:
Represents a conversation or message within a project.

Attributes:
project: ForeignKey relationship with the Project model.
user: ForeignKey relationship with the Django User model representing the sender of the message.
message_text: CharField for the content of the message.
message_type: CharField for the type of message (e.g., text, image, etc.).
timestamp: DateTimeField for the timestamp of the message.
String representation: Returns the message text.

Resources Model:
Represents a resource uploaded within a project.

Attributes:
project: ForeignKey relationship with the Project model.
resource_type: CharField for the type of the resource.
resource_link: FileField for the link to the uploaded resource.
user: ForeignKey relationship with the Django User model representing the uploader.
is_processed: BooleanField indicating whether the resource has been processed.
timestamp: DateTimeField for the timestamp of the resource upload.

PinnedItems Model:
Represents items pinned within a project (e.g., important messages).

Attributes:
project: ForeignKey relationship with the Project model.
conversation: ForeignKey relationship with the Conversation model.
user: ForeignKey relationship with the Django User model representing the user who pinned the item.
timestamp: DateTimeField for the timestamp of the pinning.

Each model is designed to facilitate collaboration and organization within a project management system, allowing users to create teams, manage projects, communicate via messages, share resources, and highlight important items.






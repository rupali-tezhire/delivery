import aws_cdk as cdk

from server_less.server_less_stack import ServerLessStack


app = cdk.App()
ServerLessStack(app, "ServerLessStack")

app.synth()

module.exports = (robot) ->
  robot.respond /help/i, (res) ->
   res.reply "\n*Infra Management Chatops Commands*\n_Command Syntax_```!service restart <service_name> on <hosts> - Restart service on remote hosts\n!service stop <service_name> on <hosts> - Stop service on remote hosts\n!status <hosts> - Show status for hosts (ansible ping module)\n!http status <hosts> - Show Service Status\n!ansible <command> - Run Ansible command on local machine\n!ws open <website> - Open website on registered Device\n!ws check <website> - Genrate snapshot of website and share```"


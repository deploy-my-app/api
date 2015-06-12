"""
GET DEPLOYS

FOREACH DEPLOYS
	FOREACH ROUTINE
		FOREACH COMMAND
			IF DEPLOY is SYNCHRONOUS 
				IF COMMAND not in RUNNING_COMMANDS
					IF URL has runned_command AND runned_status is SUCCESS AND URL has deploy_id
						COMMAND = get next command with runned_command
				FOREACH SERVER IN DEPLOY
					ping server.ip?command=COMMAND&ping_back=API_URL
			ELSE_IF DEPLOY NOT SYNCHRONOUS
				ping server.ip?command=COMMAND&ping_back=API_URL
"""
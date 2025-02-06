import datetime

# Bot configurations
bot_configs = [
    {
        "bot_name": "Chat-at-Data Coordinator",
        "agent_name": "poc-chat-at-data-coordinator",
        "start_prompt": "What capabilities do you have?"
    }, 
    {
        "bot_name": "scXpress agent (poc)",
        "agent_name": "poc-scxpress-chat",
        "start_prompt": "Can you find the number of projects in scXpress?"
    }, 
    {
        "bot_name": "Xpress agent (poc)",
        "agent_name": "poc-xpress-chat",
        "start_prompt": "Can you find the number of projects in Xpress?"
    }, 
    {
        "bot_name": "scXpress agent (senshark)",
        "agent_name": "senshark-scxpress-chat",
        "start_prompt": "Can you find the number of projects in scXpress?"
    }, 
    {
        "bot_name": "Xpress agent (senshark)",
        "agent_name": "senshark-xpress-chat",
        "start_prompt": "Can you find the number of projects in Xpress?"
    }, 
    {
        "bot_name": "Mortgages Assistant",
        "agent_name": "mortgages_assistant",
        "start_prompt": "I'm your mortgages assistant. How can I help today?",
        "session_attributes": {
            "sessionAttributes": {
                "customer_id": "123456",
                "todays_date": datetime.datetime.now().strftime("%Y-%m-%d")
            },
            "promptSessionAttributes": {
                "customer_id": "123456",
                "customer_preferred_name": "Mark",
                "todays_date": datetime.datetime.now().strftime("%Y-%m-%d")
            }
        }
    }
]

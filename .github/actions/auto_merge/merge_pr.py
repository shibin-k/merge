print("Running script to mergr PR")

def neutral_exit():
  sys.exit(0)
  
if __name__ == '__main__':
    github_token = os.environ["GITHUB_TOKEN"]
    github_repository = os.environ["GITHUB_REPOSITORY"]

    github_event_path = os.environ["GITHUB_EVENT_PATH"]
    event_data = json.load(open(github_event_path))
    
    print("Event Data")
    print(f"*** Event data {event_data}. Event path: {github_event_path}")

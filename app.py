import pandas as pd
import json
import boto3

from utils import app_constants


def run_multi_modal_prompt(bedrock_runtime, model_id, messages, max_tokens):
    body = json.dumps(
        {
            "system": app_constants.SYSTEM_PROMPT,
            "anthropic_version": app_constants.ANTHROPIC_VERSION,
            "temperature": app_constants.LLM_TEMPERATURE,
            "max_tokens": max_tokens,
            "messages": messages,
        }
    )
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
    )
    response_body = json.loads(response.get("body").read())
    return response_body


def get_chat_data(path_to_csv):
    df = pd.read_csv(path_to_csv)
    message_list = []
    for index, row in df.iterrows():

        user_message = {
            "role": "user",
            "content": [{"type": "text", "text": ""}],
        }
        assistant_message = {
            "role": "assistant",
            "content": [{"type": "text", "text": ""}],
        }

        data_dict = {"request": {}, "response": {}}
        data_dict["request"]["Question"] = row["prompt"].strip()
        data_dict["request"]["Answer"] = row["essay"].strip()

        data_dict["response"]["evaluation"] = row["evaluation"].strip()
        data_dict["response"]["band"] = row["band"].strip()

        user_message["content"][0]["text"] = json.dumps(data_dict["request"])
        assistant_message["content"][0]["text"] = json.dumps(
            data_dict["response"]
        )
        message_list.append(user_message)
        message_list.append(assistant_message)
    return message_list


def writing_task_2(question, answer):
    bedrock_runtime = boto3.client(
        "bedrock-runtime",
        region_name=app_constants.REGION_NAME,
        aws_access_key_id=app_constants.ACCESS_KEY,
        aws_secret_access_key=app_constants.SECRET_KEY,
    )
    model_id = app_constants.MODEL_ID
    max_tokens = app_constants.MAX_TOKENS
    user_message = {"role": "user", "content": [{"type": "text", "text": ""}]}
    assistant_message = {
        "role": "assistant",
        "content": [{"type": "text", "text": "{"}],
    }
    user_message["content"][0]["text"] = json.dumps(
        {"Question": question, "Answer": answer}
    )
    messages = [user_message, assistant_message]
    previous_chat = get_chat_data("ielts_writing_task_2_training_data.csv")
    messages = previous_chat + messages
    response = run_multi_modal_prompt(
        bedrock_runtime, model_id, messages, max_tokens
    )
    return eval("{" + response["content"][0]["text"])


if __name__ == "__main__":
    question = input("Enter your question: ")
    answer = input("Enter your answer: ")
    output = writing_task_2(question, answer)
    print("your overall band score is : ", output["band"])
    print("Examiner comments : ", output["evaluation"])
    print("done")

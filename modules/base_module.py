

class BaseModule:
    def create_request_body(self, schema, data_class_instance):
        data_dict = {
            key: value for key, value in data_class_instance.__dict__.items()
        }
        return schema(**data_dict).model_dump_json()
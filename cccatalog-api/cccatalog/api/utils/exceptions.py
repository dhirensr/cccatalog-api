from rest_framework import status
from rest_framework.response import Response


def input_error_response(errors):
    field = [f for f in errors]
    messages = []
    for _field in errors:
        error = errors[_field]
        for e in error:
            messages.append(e)
    messages = ' '.join(messages)

    # Don't return "non field errors" in deprecation exceptions. There is no
    # other way to recover the affected fields other than parsing the error.
    if field == ['non_field_errors']:
        split_error = messages.split(' ')
        field_idx = messages.index('Parameter') + 1
        field = [split_error[field_idx].replace("'", '')][0]

    return Response(
        status=status.HTTP_400_BAD_REQUEST,
        data={
            'error_type': 'InputError',
            'detail': f'Invalid input given for field {field}.'
            f' Hint: {messages}',
            'field': field
        }
    )

# core/utils.py
import json

def restore_form_from_session(session, form_class, data_key='contact_form_data', errors_key='contact_form_errors'):
    """
    Pops form data and errors from session, rebuilds the form with errors injected,
    and returns (form, open_modal).

    :param session:        The request.session object
    :param form_class:     The Django form class you want to reconstruct
    :param data_key:       Session key for form data
    :param errors_key:     Session key for form errors (in JSON)
    :return: (form, open_modal)
    """
    # 1) Get stored data and errors
    form_data = session.pop(data_key, None)
    form_errors_json = session.pop(errors_key, None)

    # 2) If either data or errors exist, we typically set open_modal = True
    open_modal = bool(form_data or form_errors_json)

    # 3) Build the form with initial data if present
    if form_data:
        form = form_class(initial=form_data)
    else:
        form = form_class()

    # 4) Inject errors if any
    if form_errors_json:
        errors_dict = json.loads(form_errors_json)  # Convert back from JSON
        for field_name, field_errors in errors_dict.items():
            for err in field_errors:
                # Each err is usually of the form {"message": "..."}
                form.add_error(field_name, err["message"])

    return form, open_modal

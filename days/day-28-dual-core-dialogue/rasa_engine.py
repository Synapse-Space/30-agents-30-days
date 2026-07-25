from shared_core.dialogue import RasaEngine, DialogueResponse, DialogueEngine

class EnterpriseRasaEngine(RasaEngine):
    def respond(self, message, state):
        text = message.strip()

        # If not already in an active form, start the account opening flow
        if not getattr(state, "active_form", None):
            state.active_form = "account"
            state.context["step"] = "full_name"
            return DialogueResponse(
                response="[Rasa Workflow] Starting Bank Account Application.\nStep 1/2: Please enter your Full Name:",
                engine=DialogueEngine.RASA,
                metadata={"form": "account", "step": "full_name"}
            )

        step = state.context.get("step", "full_name")

        if step == "full_name":
            state.slots["full_name"] = text
            state.context["step"] = "email"
            return DialogueResponse(
                response=f"[Rasa Workflow] Thank you, {text}.\nStep 2/2: Please enter your Email Address:",
                engine=DialogueEngine.RASA,
                metadata={"form": "account", "step": "email", "slots": state.slots}
            )

        elif step == "email":
            state.slots["email"] = text
            full_name = state.slots.get("full_name", "Valued Customer")
            email = state.slots.get("email", text)

            # Reset form state upon completion
            state.active_form = None
            state.context.clear()

            return DialogueResponse(
                response=f"✅ [Rasa Workflow] Account Application Submitted Successfully!\n• Name: {full_name}\n• Email: {email}\n• Status: Application Queued for Verification",
                engine=DialogueEngine.RASA,
                metadata={"form": "account", "status": "submitted", "slots": dict(state.slots)}
            )

        return DialogueResponse(
            response="Welcome to Enterprise Banking. How can I help you today?",
            engine=DialogueEngine.RASA,
        )
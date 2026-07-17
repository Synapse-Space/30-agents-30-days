class PublishingWorkflow:
    def run(self, adapter, page, draft):
        adaptor.open_editor(page)
        adaptor.fill_title(page, draft.title)
        adaptor.fill_body(page, draft.body)
        adaptor.save_draft(page)
class PublishingWorkflow:
    def run(self, adapter, page, draft):
        adapter.open_editor(page)
        adapter.fill_title(page, draft.title)
        adapter.fill_body(page, draft.body)
        adapter.save_draft(page)
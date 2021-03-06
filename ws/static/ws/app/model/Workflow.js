Ext.define('WS.model.Workflow', {
    extend: 'Ext.data.Model',
    fields: ['pk', 'name'],

    proxy: {
        type: 'ajax',
        api: {
            read: '/ws/workflows.json',
            update: '/static/ws/data/updateTasks.json'
        },
        reader: {
            type: 'json',
            root: 'rows',
        }
    }
});

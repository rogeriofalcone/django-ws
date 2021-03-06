Ext.define('WS.view.process.Grid', {
    extend: 'Ext.grid.Panel',
    alias: 'widget.processgrid',
    layout: 'fit',

    initComponent: function() {
        if (! this.store) {
            this.store = Ext.create('WS.store.Processes', {
                autoLoad: true,
            });
        }
        this.columns = [
            Ext.create('Ext.grid.RowNumberer'),
            {header: 'Process', dataIndex: 'name', flex: 1},
            {header: 'Type', dataIndex: 'workflow', flex: 1},
            {header: 'Started', dataIndex: 'start_date', flex: 1},
            {header: 'Ended', dataIndex: 'end_date', flex: 1},
            {header: 'Status', dataIndex: 'status', flex: 1, renderer: this.renderStatus},
        ];
        this.dockedItems = [{
            xtype: 'pagingtoolbar',
            store: this.store,
            dock: 'bottom',
            displayInfo: true,
        }];
        this.callParent(arguments);
    },

    renderStatus: function(value) {
        return Ext.String.format('<div class="x-process-status-{0}">{1}</div>', value, value);
    },
});

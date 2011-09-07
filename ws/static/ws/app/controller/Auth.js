Ext.define('WS.controller.Auth', {
    extend: 'Ext.app.Controller',
    uses: ['Ext.util.Cookies'],
    views: [
        'auth.Login',
    ],

    init: function() {
        //console.log('Initialized Tasks! This happens before the Application launch function is called');
        this.control({
            'login button[action=login]': {
                click: this.login
            }
        });
        Ext.Ajax.on('beforerequest', this.ajax_csrf);
    },

    ajax_csrf: function(conn, options) {
        if (!(/^http:.*/.test(options.url) || /^https:.*/.test(options.url))) {
            if (typeof(options.headers) == "undefined") {
                options.headers = {'X-CSRFToken': Ext.util.Cookies.get('csrftoken')};
            } else {
                options.headers.extend({'X-CSRFToken': Ext.util.Cookies.get('csrftoken')});
            }                        
        }
    },

    login: function(button) {
        console.log('clicked the login button');
        var panel = button.up('panel'),
            form = panel.down('form');
        form.submit({
            method:'POST', 
            waitTitle:'Connecting', 
            waitMsg:'Sending data...',
            success:function(){ 
                console.log('success!');
                Ext.Msg.alert('Status', 'Login Successful!');
            },

            failure: function(form, action) {
                switch (action.failureType) {
                    case Ext.form.action.Action.CLIENT_INVALID:
                        Ext.Msg.alert('Failure', 'Form fields may not be submitted with invalid values');
                        break;
                    case Ext.form.action.Action.CONNECT_FAILURE:
                        Ext.Msg.alert('Failure', 'Server communication failed');
                        break;
                    case Ext.form.action.Action.SERVER_INVALID:
                       Ext.Msg.alert('Failure', action.result.message);
               }
            }
        });
    }

});


FileBrowserHelper = {
    markItUp: false,

    show: function(markItUp) {
        this.markItUp = markItUp
        var textarea_id = $(markItUp.textarea).attr('id');
        FileBrowser.show(textarea_id, '/admin/filebrowser/browse/?pop=1&type=');
    },

    triggerInsert: function(url) {
        $(this.markItUp.textarea).trigger('insertion',
            [{replaceWith: '![[![Alternative text]!]]('+url+' "[![Title]!]")'}]);
    }
};

FileBrowserHelper = {
    markItUp: false,

    show: function(markItUp, type) {
        this.markItUp = markItUp
        var textarea_id = $(markItUp.textarea).attr('id');
        FileBrowser.show(textarea_id, '/admin/filebrowser/browse/?pop=1&type=' + type);
    },

    triggerInsert: function(url) {
        $(this.markItUp.textarea).trigger('insertion',
            [{replaceWith: '![[![Alternative text]!]]('+url+' "[![Title]!]")'}]);
    }
};

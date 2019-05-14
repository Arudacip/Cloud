var sys = arbor.ParticleSystem(200, 100, 5000);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;
var data = {
    nodes:{
    fase_1:{'color':'red','shape':'dot','label':'fase_1'},
    fase_2:{'color':'green','shape':'dot','label':'fase_2'},
    fase_3:{'color':'green','shape':'dot','label':'fase_3'},
    fase_4:{'color':'blue','shape':'dot','label':'fase_4'},
    fase_5:{'color':'blue','shape':'dot','label':'fase_5'},
    fase_6:{'color':'blue','shape':'dot','label':'fase_6'},
    fase_7:{'color':'blue','shape':'dot','label':'fase_7'},
    fase_8:{'color':'blue','shape':'dot','label':'fase_8'},
    fase_9:{'color':'blue','shape':'dot','label':'fase_9'},
    fase_a:{'color':'yellow','shape':'dot','label':'fase_a'},
    fase_b:{'color':'yellow','shape':'dot','label':'fase_b'},
    fase_c:{'color':'yellow','shape':'dot','label':'fase_c'},
    fase_d:{'color':'yellow','shape':'dot','label':'fase_d'},
    fase_end:{'color':'purple','shape':'dot','label':'fase_end'}
    },
    edges:{
        fase_1:{ fase_2:{}, fase_3:{} },
        fase_2: {fase_4:{}, fase_5:{}, fase_6:{}},
        fase_3: {fase_7:{}, fase_8:{}, fase_9:{}},
        fase_4: {fase_a:{}, fase_b: {}},
        fase_5: {fase_a:{}, fase_b: {}},
        fase_6: {fase_a:{}, fase_b: {}},
        fase_7: {fase_c:{}, fase_d: {}},
        fase_8: {fase_c:{}, fase_d: {}},
        fase_9: {fase_c:{}, fase_d: {}},
        fase_a: {fase_end:{}},
        fase_b: {fase_end:{}},
        fase_c: {fase_end:{}},
        fase_d: {fase_end:{}}
    }
    };
sys.graft(data);
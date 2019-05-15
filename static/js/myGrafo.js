var sys = arbor.ParticleSystem(200, 200, 0.5);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;
var data = {
    nodes:{
    fase_1:{'color':'red','shape':'dot','label':'fase1'},
    fase20:{'color':'green','shape':'dot','label':'fase20'},
    fase21:{'color':'green','shape':'dot','label':'fase21'},
    fase22:{'color':'green','shape':'dot','label':'fase23'},
    fase300:{'color':'blue', 'shape':'dot', 'label':'fase300'},
    fase301:{'color':'blue', 'shape':'dot', 'label':'fase301'},
    fase302:{'color':'blue', 'shape':'dot', 'label':'fase302'},
    fase303:{'color':'blue', 'shape':'dot', 'label':'fase303'},
    fase310:{'color':'blue', 'shape':'dot', 'label':'fase310'},
    fase311:{'color':'blue', 'shape':'dot', 'label':'fase311'},
    fase312:{'color':'blue', 'shape':'dot', 'label':'fase312'},
    fase313:{'color':'blue', 'shape':'dot', 'label':'fase313'},
    fase320:{'color':'blue', 'shape':'dot', 'label':'fase320'},
    fase321:{'color':'blue', 'shape':'dot', 'label':'fase321'},
    fase322:{'color':'blue', 'shape':'dot', 'label':'fase322'},
    fase323:{'color':'blue', 'shape':'dot', 'label':'fase323'},
    fase400:{'color':'yellow', 'shape':'dot', 'label':'fase400'},
    fase401:{'color':'yellow', 'shape':'dot', 'label':'fase401'},
    fase402:{'color':'yellow', 'shape':'dot', 'label':'fase402'},
    faseFinal:{'color':'purple', 'shape':'dot', 'label':'faseFinal'}
    },
    edges:{
        fase_1:{ fase20:{}, fase21:{}, fase22:{ }},
        fase20:{ fase300:{}, fase301:{}, fase302:{}, fase303:{}},
        fase21:{ fase310:{}, fase311:{}, fase312:{}, fase313:{}},
        fase22:{ fase320:{}, fase321:{}, fase322:{}, fase323:{}},
        fase400:{ fase300:{}, fase311:{}, fase322:{}, fase320:{}},
        fase401:{ fase310:{}, fase301:{}, fase323:{}, fase313:{}},
        fase402:{ fase303:{}, fase321:{}, fase302:{}, fase312:{}},
        faseFinal:{ fase400:{}, fase401:{}, fase402:{ }}
    }
    };
sys.graft(data);
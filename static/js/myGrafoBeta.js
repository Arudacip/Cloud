var sys = arbor.ParticleSystem(200, 200, 0.5);
sys.parameters({gravity:true});
sys.renderer = Renderer("#viewport") ;
var graphData = {
    nodes:{
    fase_1:{'color':data,'shape':'dot','label':'fase1'}
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
sys.graft(graphData);
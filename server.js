import http from 'node:http';
import {readFile} from 'node:fs/promises';
import {resolve, extname} from 'node:path';
const root=resolve(process.env.SERVE_DIST==='1'?'dist':'.');
http.createServer(async(req,res)=>{try{const path=resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://local').pathname));if(!path.startsWith(root+'/')&&path!==root)throw Error();const file=path===root?root+'/index.html':path;if(!['index.html','styles.css','app.js','engine.js','brand-tokens.js','visualization.js','review-deck.js'].some(name=>file===root+'/'+name))throw Error();const data=await readFile(file);res.writeHead(200,{'Content-Type':({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[extname(file)]||'application/octet-stream','X-Content-Type-Options':'nosniff'});res.end(data)}catch{res.writeHead(404);res.end('Not found')}}).listen(Number(process.env.PORT)||3000,'0.0.0.0',()=>console.log('PMP Growth OS listening on port '+(process.env.PORT||3000)));

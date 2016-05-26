from simulator import app, render_template, request, send_from_directory, os, redirect, url_for, generador, lectura, json, flash, formatingData
from werkzeug import secure_filename
from os import listdir
from os.path import isfile, join

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def init():
    return render_template('home.html')

@app.route('/helper.pdf')
def helper():
    downloads = os.path.join(app.config['HELPER'])
    return send_from_directory(directory=downloads, filename='helper.pdf')

@app.route('/showOptions')
def showOptions():
    return render_template('options.html')

@app.route('/inputData', methods=['GET', 'POST'])
def inputData():
    fdp = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] 
    if request.method == 'POST':
       scenario = request.form['selectSI']
       print(scenario)
       inputList = [request.form['wti'], request.form['wtf'], request.form['cpui'], request.form['cpuf'], request.form['memi'], request.form['memf'], request.form['neti'], request.form['netf'], request.form['revi'], request.form['revf'], request.form['slai'], request.form['slaf'], request.form['vmsi'], request.form['vmsf'], request.form['srvi'], request.form['srvf'], request.form['dci'], request.form['dcf']]
       print(inputList)      
       fdpVcpu = request.form['fdpVcpu']
       fdpVmem = request.form['fdpVmem'] 
       fdpUcpu = request.form['fdpUcpu']
       fdpUmem = request.form['fdpUmem']
       fdpUnet = request.form['fdpUnet']
       fdpVM = request.form['fdpVM']
       if fdpVcpu == '0':
           fdp[0]=[int(fdpVcpu), int(request.form['fUniformVcpu']), int(request.form['tUniformVcpu'])]
       elif fdpVcpu == '1':
           fdp[0]=[int(fdpVcpu), int(request.form['lambdaVcpu']), 0]
       elif fdpVcpu == '2':
           fdp[0]=[int(fdpVcpu), float(request.form['muVcpu']), float(request.form['sigmaVcpu'])]
       if fdpVmem == '0':
           fdp[1]=[int(fdpVmem), int(request.form['fUniformVmem']), int(request.form['tUniformVmem'])]
       elif fdpVmem == '1':
           fdp[1]=[int(fdpVmem), int(request.form['lambdaVmem']), 0]
       elif fdpVmem == '2':
           fdp[1]=[int(fdpVmem), float(request.form['muVmem']), float(request.form['sigmaVmem'])]
       if fdpUcpu == '0':
           fdp[3]=[int(fdpUcpu), int(request.form['fUniformUcpu']), int(request.form['tUniformUcpu'])]
       elif fdpUcpu == '1':
           fdp[3]=[int(fdpUcpu), int(request.form['lambdaUcpu']), 0]
       elif fdpUcpu == '2':
           fdp[3]=[int(fdpUcpu), float(request.form['muUcpu']), float(request.form['sigmaUcpu'])]
       if fdpUmem == '0':
           fdp[4]=[int(fdpUmem), int(request.form['fUniformUmem']), int(request.form['tUniformUmem'])]
       elif fdpUmem == '1':
           fdp[4]=[int(fdpUmem), int(request.form['lambdaUmem']), 0]
       elif fdpUmem == '2':
           fdp[4]=[int(fdpUmem), float(request.form['muUmem']), float(request.form['sigmaUmem'])]
       if fdpUnet == '0':
           fdp[5]=[int(fdpUnet), int(request.form['fUniformUnet']), int(request.form['tUniformUnet'])]
       elif fdpUnet == '1':
           fdp[5]=[int(fdpUnet), int(request.form['lambdaUnet']), 0]
       elif fdpUnet == '2':
           fdp[5]=[int(fdpUnet), float(request.form['muUnet']), float(request.form['sigmaUnet'])]
       if fdpVM == '0':
           fdp[6]=[int(fdpVM), int(request.form['fUniformVM']), int(request.form['tUniformVM'])]
       elif fdpVM == '1':
           fdp[6]=[int(fdpVM), int(request.form['lambdaVM']), 0]
       elif fdpVM == '2':
           fdp[6]=[int(fdpVM), float(request.form['muVM']), float(request.form['sigmaVM'])]
       print(fdp)
       #formatInput(scenario, inputList, fdp)
       if request.form['submit'] == 'generate':
          generador.generate_env(scenario, inputList, fdp, None)
          return redirect(url_for('download',
                                       filename="out.txt"))
       elif request.form['submit'] == 'download':
          formatingData.formatData(scenario, inputList, fdp)
          return redirect(url_for('download_input',
                                       filename="input"))
    return render_template('input.html')

@app.route('/uploadFile', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        scenario = -1
        file = request.files['file']
        if file and allowed_file(file.filename) and scenario:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                        filename=filename, scenario=scenario))
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    scenario = request.args['scenario']
    if filename :
        generador.generate_env(scenario, 0, [], filename)
        return redirect(url_for('download',
                                    filename=filename))
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
   
@app.route('/input.txt', methods=['GET', 'POST'])
def download_input():
    downloads = os.path.join(app.config['INPUT_DATA'])
    return send_from_directory(directory=downloads, filename='input')

@app.route('/out.txt', methods=['GET', 'POST'])
def download():
    downloads = os.path.join(app.config['DOWNLOAD_FOLDER'])
    return send_from_directory(directory=downloads, filename='out')

@app.route('/benchmark')
def benchmark():
    scenario_files = []
    scenario_files_number = []
    for x in range(0, 16):
        file_path = os.path.join(app.config['BENCHMARK'] + 'scenario' + str(x))
        aux = [f for f in listdir(file_path) if isfile(join(file_path, f))]
        scenario_files.insert(x, aux)
        scenario_files_number.append(len(aux))
    return render_template('benchmark.html', title = 'Benchmark',
                        scenario_files_number = scenario_files_number,
                        scenario_files = scenario_files)



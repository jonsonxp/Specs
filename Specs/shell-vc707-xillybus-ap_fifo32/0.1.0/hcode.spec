{
  "name": "shell-vc707-xillybus-ap_fifo32",
  "type": "shell",
  "version": "0.1.0",
  "summary": "A hCODE shell based on xillybus-eval-vertex7-1.2c PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-vc707-xillybus-ap_fifo32.git",
    "tag": "0.1.0"
  },
  "platforms": {
    "vc707": "0.0.0"
  },
  "ides": [
    {"vivado2015.3": true},
    {"vivado2015.4": true}
  ],
  "properties": {
    "max-clock": "250MHz",
    "host-fpga": {
        "name": "xillybus-eval-virtex7-1.2c",
        "interface": {
            "protocol" : "axi-stream",
            "datawidth" : "32"
        }
    }
  }
}

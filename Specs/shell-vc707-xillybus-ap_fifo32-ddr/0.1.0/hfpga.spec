{
  "name": "shell-vc707-xillybus-vivado20153",
  "type": "shell",
  "version": "0.1.0",
  "summary": "A hCODE shell based on xillybus-eval-vertex7-1.2c PCIe module and ddr3 interface.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-vc707-xillybus-ap_fifo32-ddr-0.1.0.git",
    "tag": "0.1.0"
  },
  "platforms": {
    "vc707": "all"
  },
  "ides": {
    "version": "vivado2015.3",
    "version": "vivado2015.4"
  },
  "properties": {
    "max-clock": "250MHz",
    "host-fpga": {
        "name" : "xillybus-eval-virtex7-1.2c",
        "interface" : 
          {
            "protocol" : "axi-stream",
            "datawidth" : "32"
          }
    },
    "fpga-ddr": {
        "name" : "xilinx-mig",
        "interface" :
          {
            "protocol" : "axi-master",
            "datawidth" : "32",
            "addresswidth" : "32"
          }
      }
  }
}

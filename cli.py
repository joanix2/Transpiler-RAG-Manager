import os
import click
from external.JTx2 import convert_xml_to_json, compile_json, transpile_xml_or_json, build_infrastructure
from src.watcher import start_watching
from external.jinja_templates import TEMPLATES_DIR, TEMPLATES_PATH, MACROS_PATH

print(TEMPLATES_DIR)

INFRASTRUCTURE = os.path.join("output","infrastructure.yml")

@click.group()
def cli():
    """
    CLI pour la gestion des templates et des projets.
    """
    pass

@cli.command()
@click.argument("xml_file", type=click.Path(exists=True), required=True)
@click.option("--json-file", "-j", type=click.Path(), default=None, help="Fichier JSON de sortie. Par défaut, même nom que le fichier XML avec extension .json.")
def convert(xml_file, json_file):
    """
    Convertit un fichier XML en JSON.

    Options :
        xml_file : Fichier XML source.
        --json-file, -j : Fichier JSON de sortie (facultatif).
                         Par défaut, le JSON aura le même nom et se trouvera dans le même répertoire que le fichier XML.
    """
    convert_xml_to_json(xml_file, json_file)

@cli.command()
@click.argument("input_file", type=click.Path(exists=True), default="main.json")
@click.option("--type", "-t", type=str, default="default", help="Choix du type de compilation du premier nœud.")
@click.option("--output", "-o", type=click.Path(), default=INFRASTRUCTURE, help="Répertoire de sortie pour les fichiers générés.")
def compile(input_file, type, output):
    """
    Traite un fichier JSON et génère des fichiers à partir de templates.

    Arguments :
        INPUT_FILE : Le fichier JSON à traiter (par défaut : main.json).

    Options :
        --type, -t : Choix du type de compilation du premier nœud (par défaut : 'default').
        --output-dir, -o : Répertoire de sortie pour les fichiers générés (par défaut : 'output').
    """
    click.echo(f"Processing JSON file: {input_file}")
    click.echo(f"Output file: {output}")

    compile_json(TEMPLATES_DIR, input_file, type, output)

@cli.command()
@click.option("--config-file", "-c", type=click.Path(exists=True), default=INFRASTRUCTURE, help="Fichier YAML décrivant l'arborescence.")
def build(config_file):
    """
    Génère une arborescence de projet à partir d'un fichier YAML.

    Options :
        --config-file, -c : Fichier YAML décrivant la structure du projet (par défaut : 'infrastructure.yml').
    """
    click.echo(f"Loading configuration from: {config_file}")
    build_infrastructure(config_file)

@cli.command()
@click.argument("input_file", type=click.Path(exists=True), default="main.xml")
@click.option("--type", "-t", type=str, default="default", help="Choix du type de compilation du premier nœud.")
@click.option("--output", "-o", type=click.Path(), default=INFRASTRUCTURE, help="Répertoire de sortie pour les fichiers générés.")
def run(input_file, type, output):
    transpile_xml_or_json(TEMPLATES_DIR, input_file, type, output)

@cli.command()
@click.argument("target_file", type=click.Path(exists=True), default="main.xml")
def start(target_file):
    """
    Démarre l'observateur qui surveille les fichiers et recompile automatiquement.

    Arguments :
        target_file : Le fichier XML ou JSON à traiter.
    """
    click.echo(f"👀 Surveillance activée sur : {target_file} et le dossier templates/\n")
    start_watching([TEMPLATES_PATH, MACROS_PATH], target_file)

if __name__ == "__main__":
    cli()

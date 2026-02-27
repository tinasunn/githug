#!/usr/bin/env python3

import click
from git import Repo, exc
import yaml

try:
    repo = Repo('.')
except exc.InvalidGitRepositoryError:
    click.echo("No git repo")
    exit(1)
untracked = repo.untracked_files
unstaged = [diff.a_path for diff in repo.index.diff(None)]#compares to current dir
staged = [diff.a_path for diff in repo.index.diff(repo.head.commit)]


@click.group()
@click.option('--dry_run', is_flag=True, help='Simulate tool result output')
@click.pass_context
def gitwrap(ctx, dry_run):
    ctx.ensure_object(dict)
    ctx.obj['dry_run'] = dry_run

def run_dry(ctx):
    click.echo(f"dry_run: {ctx.obj['dry_run']} \n\naction: {ctx.command.name}")

def out_yaml(data):
    if len(data) != 0:
        return yaml.dump(data, default_flow_style=False, sort_keys=False)


@gitwrap.command()
@click.pass_context
@click.option('--yes', is_flag=True, help='Skip confirmation prompt.')
def clean(ctx, yes):    
    """prompt user before deleting any files
    --yes flag to skip prompt
    --dry-run to list untracted files that would be deleted without deleting"""
    if ctx.obj['dry_run']:
        run_dry(ctx)
        click.echo("\nfiles: \n")
        # for i in untracked:
            # click.echo(f" - {i}\n")
        click.echo(f"{out_yaml(untracked)}")
    else:
        if not yes:
            confirm = click.prompt(f"This will delete {len(untracked)} files. Continue? [y/n]", default="no")
            if confirm.lower() != 'y':
                click.echo("Oops! Aborting clean operation.")
                return
        repo.git.clean('-fd')
        click.echo("Untracked files deleted.")

@gitwrap.command()
@click.pass_context
def status(ctx):
    if ctx.obj['dry_run']:
        run_dry(ctx)
    else: 
        click.echo(f"action: {ctx.command.name}")
    click.echo(f"\nbranch: {repo.active_branch.name} \n\nstaged_files: \n{out_yaml(staged)} \nunstaged_files: \n{out_yaml(unstaged)} \n\nuntracked_files: \n{out_yaml(untracked)}")

if __name__ == '__main__':
    gitwrap()

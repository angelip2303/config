source $HOME/.config/nvim/vim-plug/plugins.vim

" Completion
call deoplete#custom#var('omni', 'input_patterns',{
    \ 'tex': g:vimtex#re#deoplete
    \})

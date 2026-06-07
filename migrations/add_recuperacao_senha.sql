-- Adicionar campos para recuperação de senha na tabela usuarios
ALTER TABLE usuarios ADD COLUMN codigo_recuperacao VARCHAR(6) NULL;
ALTER TABLE usuarios ADD COLUMN codigo_expiracao DATETIME NULL;

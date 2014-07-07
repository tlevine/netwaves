{-# LANGUAGE ScopedTypeVariables #-}

-- http://rosettacode.org/wiki/Bitmap/Write_a_PPM_file#Haskell
 
module Bitmap.Netpbm(readNetpbm, writeNetpbm) where
 
import Bitmap
import Data.Char
import System.IO
import Control.Monad
import Control.Monad.ST
import Data.Array.ST
 
writeNetpbm :: forall c. Color c => FilePath -> Image RealWorld c -> IO ()
writeNetpbm path i = withFile path WriteMode $ \h -> do
    let w = hPutStrLn h
    w $ magicNumber
    w $ show width ++ " " ++ show height
    unless (null maxval) (w maxval)
    stToIO (getPixels i) >>= hPutStr h . toNetpbm
  where magicNumber = "P6"

main = do putStrLn "h"
